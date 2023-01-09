#!/usr/bin/perl
#
#by Kristin Y. Rozier
#
#     This program generates a test set of MTL formulas using methods inspired by those described in "Improved automata generation for linear temporal logic" by Daniele, Guinchiglia, and Vardi.
#
#     The formulas are written in a standard format; it is presumed that they will be converted to any tool-specific format necessary after having been read in by the appropriate program.
#
# Inputs: (all are required; order matters)
#      L : formula length
#      N : number of variables (named a0, a1, ...)
#      P : probability of choosing temporal operators 
#      S : the starting value of every generated bound. If S = 0, every bound starts from 0.
#      M : generate bounds <= M (M is maximum delta between i and j in Z[i,j])
#      T : max trace length; mission-time formulas must have end bounds < T (T is max value of j)
#      (--help will produce a usage message)
#      no inputs: just generate all values of L, N, and P for default value of M
#
# Outputs: (INCOMPLETE)
#
# NOTE: Any temporal operator will randomly appear 1 of 3 ways: Z, Z[i], Z[i,j]
#
# Usage: generateRandomFormulas_MTLMmaxT.pl

# Modifications by Gokul: Added a random time scale generator to append to each temporal 
# operator
#
# Each atomic should have only one type, so force atomics as G[0,0,a] a0, for example as the initial seed formula
# Next all following nodes in the AST of the formula has only preceding or coarser time scales (as only inflating projections exist)
# Also, two sides of a binary operator do not have a time scale
# Also, atomic props do not need a leading evaluation operator, like G[0,0,b](a0 & a1).


use FileHandle;      #for open() 
#use warnings;
#use strict;




#################### Argument Setup ####################

#Check for correct number and type of command line arguments

if ($ARGV[0] =~ /--help/) {
    die "generateRandomFormulas_MTL.pl: \n\tWith no arguments: generate a wide range of formula files containing MTL formulas.\n\tWith 3 arguments: generate files for specified L, N, P, S, M, T (order matters).\n";
} #end if

$S = 10; #default value for S (not starting from 0)

$M = 6; #default value for M

$T = 6; #default value for T
@times = ("d","c","b","a");
# if ($ARGV[0] =~ /-useR/i) {
#     $useR = 1; 
#     print "Creating two directories, with and without 'R'...\n";
#     shift(@ARGV); #remove this flag
# } #end if
# die "ARGV is now @ARGV";

if (@ARGV == 5) {
    print "Reading command-line arguments:\n";
    ($L, $n, $P, $M, $T) = @ARGV;
    print "L = $L; N = $n; P = $P; S = $S; M = $M; T = $T\n";
    if (($L !~ /^\d+\.?\d*$/) 
	|| ($n !~ /^\d+\.?\d*$/) 
	|| ($P !~ /^\d+\.?\d*$/)
	|| ($S !~ /^\d+\.?\d*$/)
	|| ($M !~ /^\d+\.?\d*$/)
	|| ($L < 1)
	|| ($n < 1) 
	|| ($P < 0)
	|| ($P > 1) 
	|| ($M < 1)
	|| ($T < 1)
	) {
	die "Require 5 numerical arguments: L, N, P, M, T\n";
    } #end if
} #end if

elsif (@ARGV != 0) {
    die "Usage: generateRandomFormulas_MTL.pl [optional: specify all of L, N, P, M, and T in that order]\n";
} #end elsif

else {print "Generating formulas for ranges of L, N, P, M, and T ...\n";}


#Set the directory where all of the formulas will be stored
$formula_dir = "./random";

if ($S == 0) {
    $formula_dir = "./random0";
}


#If the formula directory doesn't exist, create it
if (! (-d $formula_dir) ) {
    mkdir("$formula_dir", 0755) or die "Cannot mkdir $formula_dir: $!";
} #end if
elsif (! (-w $formula_dir) ) { #check for write permission
    die "ERROR: formula directory $formula_dir is not writable!";
} #end elseif

#################### Generation of Formulas ####################

### Set up the generation variables

$F = 5; #number of formulas to generate in one test set
print "F is $F\n";
print OUT "F is $F\n";

@N = qw(a0 a1 a2 a3); #array of variables
$n1 = @N;

print "N is @N\n";
print "n1 is $n1\n";
print OUT "N is @N\n";

#@Llist = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100);
#@Llist = (20, 40, 60, 80, 100);
@Llist = (5, 10, 15);
print "L = (@Llist)\n";
print OUT "L = (@Llist)\n";

#@Plist = (1/3, 0.5, 0.95); #array of probabilities to try
@Plist = (0.5); #array of probabilities to try
print "P = (@Plist)\n";
print OUT "P = (@Plist)\n";




#Note: No R operator in MTL
@Toperators = ("G", "F", "U");
@Poperators = ("!", "&", "|");
$num_unary_temporal_ops = 2;
$num_temporal_ops = 3;
$num_prop_ops = 3;
#order is very important here: unary temporal ops, binary temporal ops, then ! then binary ops


#####################################################################
#
# Functions: 
#    
#    generate_bounds: generates the bounds for one temporal operator 
#    generate_formula: generates one formula
#
#####################################################################


### Define a function to use to generate bounds for one temporal operator
### Future option: allow one input (1,2,3) to determine what type of bounds with the default being the current behavior of randomly choosing which type of bounds

sub generate_bounds {
    my $this;
    my $timeName = $_[0];
    print("\n Time name : $timeName \n");
    my $M_num = int(rand(3)); #Choose between the 3 common formula scenarios:
    if ($S == 0) {
        $M_num = 1;
    }	
    if ($M_num == 1) { #1) Make the bounds 0 ... num
	    my $first_num = int(rand($M));
	    $this = "[0,$first_num,${timeName}]"; #M single bound
    } elsif ($M_num == 2) { #2) Make the bounds num1 ... num2
	    my $first_num = int(rand($M));
	    my $bound = $M - $first_num;
	    my $second_num = $first_num + int(rand($bound)); #ensure 2nd num is >= 1st
	    $this = "[${first_num},${second_num},${timeName}]"; #M double bound
    } else { #3) Make the bounds num1 ... T
	    my $first_num = int(rand($M));
	    my $first_num = ${T}-${first_num};
	    if ($first_num < 0) { $first_num = 0; } #make sure the lower bound is positive
	    $this = "[$first_num,$T,${timeName}]"; #max trace bound
    } #end if

    return ($this);
    
} #end generate_bounds


### Define a recursive function to use to generate each formula
sub generate_formula {
    my $L = $_[0];
    my $S;
    my $op;
    my $this;
    my $bound;
    my $timeName;
    my $timeNameT;
    my $timeNameS;
    my $index;
    my $Shalf;
    my $Thalf;
    my $recur;
    my $var_num;
    if ($L <= 2) { #randomly choose one variable
        print("n is $n1\n");
        $var_num = int(rand($n1));
        if ($var_num == 0){
            $this = "G[0,0,a] (a${var_num})";
            $timeName = 3;    
        } elsif ($var_num == 1){
            $this = "G[0,0,b] (a${var_num})"; 
            $timeName = 2;   
        } elsif ($var_num == 2){
            $this = "G[0,0,c] (a${var_num})"; 
            $timeName = 1;   
        } elsif ($var_num == 3){
            $this = "G[0,0,d] (a${var_num})";    
            $timeName = 0;
        }
        #print STDERR "this($this) = N[$randn] for n($n)\n";
        print("In ", __LINE__ , ", formula is $this ; time is $timeName .\n");
        # $pauser = <>;
        return ($this,$timeName);
    } else { #$L > 2
	    #choose an operator $op
        $r = rand; #r is a random variate [0, 1)
        #choose an operator with certain probabilities...
        if ($r < $P) {
            #pick which temporal operator
            $i = int(rand($num_temporal_ops));
            $op = $Toperators[$i]; #because temporal operators are all first in the list
            $this = $op; #save operator in this
            my $isBinary;
            if ($op eq "U") { #binary operators
                #choose S such that 1 <= S <= L - 2
                $isBinary = 1;
                my $Lminus2 = $L - 2;
                my $S = int(1+rand($Lminus2));
                my $T = $L - $S - 1;                
                ($Shalf,$timeNameS) = &generate_formula($S);
                ($Thalf,$timeNameT) = &generate_formula($T);
                #Decide on M-bounds
                
	        } else { #unary temporal operators
                $isBinary = 0;
		        my $Lminus1 = $L - 1;
		        ($recur,$timeName) = &generate_formula($Lminus1);                
                #Decide on M-bounds
                
	        } #end else unary operator
            if ($isBinary){
                my $index = ($timeNameT < $timeNameS) ? int(rand($timeNameT)) : int(rand($timeNameS));
                $bound = generate_bounds($times[$index]);            
                $this = $this . $bound;
                $this = "((".$Shalf .") $this (" .$Thalf."))";
                print("In ", __LINE__ , " , formula is $this ; timeT is $timeNameT ; timeS is $timeNameS ; index is $index ; op is $op .\n");
                # $pauser = <>;
                return ($this,$index);
            } else {
                $index = int(rand($timeName));
                $bound = generate_bounds($times[$index]);
                $this = $this.$bound;
		        $this = "($this (" .$recur ."))";
                print("In ", __LINE__ , " formula is $this ; time is $timeName ; index is $index .\n");
                # $pauser = <>;
		        return ($this,$index);
            }
            
	    } else { #choose non-temporal operator
            #pick which non-temporal operator
            $i = int(rand($num_prop_ops));
            $op = $Poperators[$i];
            
            if ($op eq "!") { #the only non-temporal unary operator
                my $Lminus1 = $L - 1;
                ($recur,$timeName) = &generate_formula($Lminus1);
                $index = $timeName;
                $this = "(! (" .$recur ."))";
                print("In ", __LINE__ , " formula is $this ; time is $timeName; index is $index .\n");
                # $pauser = <>;
                return ($this,$timeName);
            } else { #binary op
                #choose S such that 1 <= S <= L - 2
                my $Lminus2 = $L - 2;
                $S = int(1+rand($Lminus2));
                my $T = $L - $S - 1;
                ($Shalf,$timeNameS) = &generate_formula($S);
                ($Thalf,$timeNameT) = &generate_formula($T);		
                $index = ($timeNameT < $timeNameS) ? $timeNameT : $timeNameS;
                $this = "((".$Shalf .") $op (" .$Thalf."))";
                print("In ", __LINE__ , " formula is $this ; timeT is $timeNameT ; timeS is $timeNameS ; index is $index .\n");
                # $pauser = <>;
                return ($this,$index);
            }
        } 
    } 
}


##################################################################
#
# Main Program: 
# 
#    Generate output files, each containing a set of formulas with
#       the same L, N, P, M values,.
#
#
##################################################################


if (@ARGV == 5) {

    print "\n\nN = $n, L = $L, P = $P, M = $M; T - $T:\n";

    $FormFile2 = "randomTest.mltlm";
    open(ALLFORMULAS, ">$FormFile2") or die "Could not open $FormFile2";
    for ($f = 1; $f <= $F; $f++) { #generate $F formulas
    
    #Create an output file for each set of formulas data
    #$FormFile = "${formula_dir}/P${P}N${n}L${L}M${M}T${T}-${f}.mltlm";
    #open(FORMULAS, ">$FormFile") or die "Could not open $FormFile";
    # print("In 313, time is $time, array is " . join(", ", @times));
    ## $pauser = <>;
	($formula,$time) = &generate_formula($L);
	#print FORMULAS "$formula\n";
	print ALLFORMULAS "$formula;\n";
	#print STDERR "End: $formula\n";
    
    #close(FORMULAS) or die "Could not close $FormFile";
    } #end for each formula
    
    close(ALLFORMULAS) or die "Could not close $FormFile2";
    #return; #exit since we just needed to generate this one set
    die;
} #end if


#################### Generate the sets of formulas ####################

$FormFile2 = "randomTest.mltlm";
open(ALLFORMULAS, ">$FormFile2") or die "Could not open $FormFile2";

for ($n = 1; $n <= @N; $n++) { #for n variables

    for ($l = 0; $l < @Llist; $l++) { #for each length
	$L = $Llist[$l];

	for ($p = 0; $p < @Plist; $p++) { #for each probability
	    $P = $Plist[$p];
	    
	    print "\n\nN = $n, L = $L, P = $P, M = $M, T = $T:\n";
	     

	    for ($f = 1; $f <= $F; $f++) { #generate $F formulas
		
		#Create an output file for each set of formulas data
	    #$FormFile = "${formula_dir}/P${P}N${n}L${L}M${M}T${T}-${f}.mltlm";
	    #open(FORMULAS, ">$FormFile") or die "Could not open $FormFile";
        # print("In 355, time is $time, array is " . join(", ", @times));
        ## $pauser = <>;
		($formula,$time) = &generate_formula($L);
		print  "Formula: G[0,0,$times[$time]]$formula\n";
		print ALLFORMULAS "G[0,0,$times[$time]]$formula;\n";
		#close(FORMULAS) or die "Could not close $FormFile";
	    } #end for each formula

	    
	    
	} #end for each temporal probability

    } #end for each length

} #end for n variables

close(ALLFORMULAS) or die "Could not close $FormFile2";